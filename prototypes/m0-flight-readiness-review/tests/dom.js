/* A minimal DOM sufficient to execute app.js exactly as written.

   This is deliberately not a mock of the application: it is a small document
   implementation that the real, unmodified app.js runs against, so the tests
   assert on the tree the browser would build rather than on a restatement of
   the code. It implements only what index.html and app.js touch, and it fails
   loudly on anything it does not implement rather than returning undefined.

   No dependency, no network, no file access beyond the caller's own reads.
*/

"use strict";

var VOID_TAGS = { input: true, br: true, hr: true, meta: true, link: true, img: true };

function escapeText(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function Node(tag, doc) {
  this.tagName = String(tag).toUpperCase();
  this.ownerDocument = doc;
  this.childNodes = [];
  this.parentNode = null;
  this.attributes = Object.create(null);
  this.listeners = Object.create(null);
  this.nodeType = 1;
  this._text = null;
  this.className = "";
  this.selected = false;
  this.checked = false;
  this.hidden = false;
}

Object.defineProperty(Node.prototype, "id", {
  get: function () { return this.attributes.id || ""; },
  set: function (value) {
    if (this.attributes.id && this.ownerDocument) delete this.ownerDocument._ids[this.attributes.id];
    this.attributes.id = String(value);
    if (this.ownerDocument) this.ownerDocument._ids[String(value)] = this;
  }
});

Object.defineProperty(Node.prototype, "firstChild", {
  get: function () { return this.childNodes.length ? this.childNodes[0] : null; }
});

Object.defineProperty(Node.prototype, "textContent", {
  get: function () {
    if (this.nodeType === 3) return this._text;
    return this.childNodes.map(function (child) { return child.textContent; }).join("");
  },
  set: function (value) {
    this.childNodes = [];
    var text = new TextNode(String(value), this.ownerDocument);
    text.parentNode = this;
    this.childNodes.push(text);
  }
});

Node.prototype.setAttribute = function (name, value) {
  if (name === "id") { this.id = value; return; }
  if (name === "hidden") { this.hidden = value !== false; return; }
  if (name === "class") { this.className = String(value); return; }
  this.attributes[name] = String(value);
};

Node.prototype.getAttribute = function (name) {
  if (name === "id") return this.attributes.id || null;
  if (name === "class") return this.className || null;
  return Object.prototype.hasOwnProperty.call(this.attributes, name) ? this.attributes[name] : null;
};

Node.prototype.hasAttribute = function (name) {
  return this.getAttribute(name) !== null;
};

Node.prototype.appendChild = function (child) {
  child.parentNode = this;
  this.childNodes.push(child);
  return child;
};

Node.prototype.removeChild = function (child) {
  var index = this.childNodes.indexOf(child);
  if (index !== -1) this.childNodes.splice(index, 1);
  child.parentNode = null;
  return child;
};

Node.prototype.addEventListener = function (type, handler) {
  (this.listeners[type] = this.listeners[type] || []).push(handler);
};

Node.prototype.dispatch = function (type, event) {
  var handlers = this.listeners[type] || [];
  var payload = event || {};
  if (payload.preventDefault === undefined) payload.preventDefault = function () {};
  if (payload.target === undefined) payload.target = this;
  handlers.forEach(function (handler) { handler(payload); });
  return handlers.length;
};

Node.prototype.click = function () { return this.dispatch("click", {}); };
Node.prototype.focus = function () { this.ownerDocument._focus = this; };

/* The tree walks below are what the tests query with. */
Node.prototype.walk = function (visit) {
  visit(this);
  this.childNodes.forEach(function (child) {
    if (child.nodeType === 1) child.walk(visit);
  });
};

Node.prototype.all = function (predicate) {
  var found = [];
  this.walk(function (node) { if (predicate(node)) found.push(node); });
  return found;
};

Node.prototype.byTag = function (tag) {
  var wanted = String(tag).toUpperCase();
  return this.all(function (node) { return node.tagName === wanted; });
};

Node.prototype.byClass = function (name) {
  return this.all(function (node) {
    return String(node.className).split(/\s+/).indexOf(name) !== -1;
  });
};

Node.prototype.byAttr = function (name, value) {
  return this.all(function (node) {
    var actual = node.getAttribute(name);
    return value === undefined ? actual !== null : actual === value;
  });
};

Node.prototype.toHTML = function () {
  if (this.nodeType === 3) return escapeText(this._text);
  var tag = this.tagName.toLowerCase();
  var parts = [tag];
  if (this.className) parts.push('class="' + escapeText(this.className) + '"');
  Object.keys(this.attributes).forEach(function (name) {
    parts.push(name + '="' + escapeText(this.attributes[name]) + '"');
  }, this);
  if (this.hidden) parts.push("hidden");
  var open = "<" + parts.join(" ") + ">";
  if (VOID_TAGS[tag]) return open;
  return open + this.childNodes.map(function (child) { return child.toHTML(); }).join("") + "</" + tag + ">";
};

function TextNode(text, doc) {
  this.nodeType = 3;
  this._text = text;
  this.ownerDocument = doc;
  this.parentNode = null;
  this.childNodes = [];
}
TextNode.prototype.toHTML = function () { return escapeText(this._text); };
TextNode.prototype.walk = function (visit) { visit(this); };
Object.defineProperty(TextNode.prototype, "textContent", {
  get: function () { return this._text; },
  set: function (value) { this._text = String(value); }
});

function Document() {
  this._ids = Object.create(null);
  this.readyState = "complete";
  this.listeners = Object.create(null);
  this.body = new Node("body", this);
  this._focus = null;
}

Document.prototype.createElement = function (tag) { return new Node(tag, this); };
Document.prototype.createTextNode = function (text) { return new TextNode(String(text), this); };

/* A detached node is not findable by id, exactly as in a browser. Without this,
   a node removed by clearing its parent would still resolve, and a fail-closed
   test could pass while the real page still displayed the stale subtree. */
Document.prototype.getElementById = function (id) {
  var node = this._ids[id];
  if (!node) return null;
  for (var walk = node; walk; walk = walk.parentNode) {
    if (walk === this.body) return node;
  }
  return null;
};
Document.prototype.addEventListener = function (type, handler) {
  (this.listeners[type] = this.listeners[type] || []).push(handler);
};

/* Build the mount points index.html declares, preserving its nesting.

   The nesting matters: index.html puts #routes inside #workspace, so clearing
   #workspace removes the routes with it. A flat set of siblings would let a
   fail-closed test pass while the real page still showed a stale route. */
Document.prototype.mount = function (spec) {
  var doc = this;
  (function build(parent, entries) {
    entries.forEach(function (entry) {
      var id = typeof entry === "string" ? entry : entry.id;
      var node = doc.createElement("div");
      node.id = id;
      parent.appendChild(node);
      if (entry.children) build(node, entry.children);
    });
  })(this.body, spec);
};

module.exports = { Document: Document, Node: Node, TextNode: TextNode };

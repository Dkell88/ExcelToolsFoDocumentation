// preload.js
const { contextBridge } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  // expose safe APIs if needed
});

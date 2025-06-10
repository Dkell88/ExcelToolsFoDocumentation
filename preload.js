// // preload.js
// const { contextBridge } = require('electron');

// contextBridge.exposeInMainWorld('electron', {
//   // expose safe APIs if needed
// });

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  selectFile: () => ipcRenderer.invoke('select-file'),
});


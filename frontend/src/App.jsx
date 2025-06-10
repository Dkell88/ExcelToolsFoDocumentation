import { useState } from 'react';

function App() {
  const [filePath, setFilePath] = useState('');

  const handleSelectFile = async () => {
    const path = await window.electron.selectFile();
    setFilePath(path);
  };

  const handleFunction = (fnNumber) => {
    alert(`Function ${fnNumber} clicked for file:\n${filePath}`);
    // Later: send path and fnNumber to Python backend
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Excel Tool</h1>
      <button onClick={handleSelectFile}>Select Excel File</button>
      {filePath && <p>Selected file: {filePath}</p>}
      <div style={{ marginTop: '1rem' }}>
        <button onClick={() => handleFunction(1)}>Function 1</button>
        <button onClick={() => handleFunction(2)}>Function 2</button>
        <button onClick={() => handleFunction(3)}>Function 3</button>
      </div>
    </div>
  );
}

export default App;

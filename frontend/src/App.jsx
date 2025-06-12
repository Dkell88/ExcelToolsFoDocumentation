import { useState } from 'react';

function App() {
  const [filePath, setFilePath] = useState('')
  const [message, setMessage] = useState('')

  const callApi = async (endpoint) => {
    setMessage('Running...')
    try {
      const res = await fetch(`http://localhost:5000/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_path: filePath })
      })
      const data = await res.json()
      if (data.success) {
        setMessage(JSON.stringify(data))
      } else {
        setMessage('Error running command')
      }
    } catch (err) {
      setMessage('Request failed')
    }
  }

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
      <div style={{ marginTop: '0.5rem' }}>
            <button onClick={() => callApi('extract')}>Extract IO List</button>
            <button onClick={() => callApi('convert')} style={{ marginLeft: '0.5rem' }}>Convert to CSV</button>
      </div>
      <p>{message}</p>
    </div>
  )
}

export default App;

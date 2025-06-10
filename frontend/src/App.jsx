import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0)
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
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((c) => c + 1)}>count is {count}</button>
        <div style={{ marginTop: '1rem' }}>
          <input
            placeholder="Excel file path"
            value={filePath}
            onChange={(e) => setFilePath(e.target.value)}
            style={{ width: '300px' }}
          />
          <div style={{ marginTop: '0.5rem' }}>
            <button onClick={() => callApi('extract')}>Extract IO List</button>
            <button onClick={() => callApi('convert')} style={{ marginLeft: '0.5rem' }}>Convert to CSV</button>
          </div>
        </div>
        <p>{message}</p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App;

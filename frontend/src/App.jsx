import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

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
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
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
    </>
  )
}

export default App

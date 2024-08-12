import React, { useState } from 'react';
import './App.css'; 

function App() {
    const [file, setFile] = useState(null);
    const [summary, setSummary] = useState('');
    const [error, setError] = useState(''); 

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log("Button clicked");
        if (!file) {
            setError('Please select a file.');
            return;
        }

        setError('');
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://127.0.0.1:5000/upload/', {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }

            const data = await response.json();
            console.log(data);
            console.log(data["summary"]);
            setSummary(data.summary);
        } catch (error) {
            console.error('Error details:', error); 
            setError(`Error: ${error.message}`);
        }
    };

    return (
        <div className="file-upload-container">
            <h1>File Upload and Summarization</h1>
            <form onSubmit={handleSubmit} className="file-upload-form">
                <input 
                    type="file" 
                    onChange={handleFileChange} 
                    className="file-input"
                />
                <button 
                    type="submit" 
                    className="upload-button"
                    disabled={!file} 
                >
                    Upload and Summarize
                </button>
            </form>
            {summary && (
                <div className="summary-container">
                    <h2>Summary:</h2>
                    <p>{summary}</p>
                </div>
            )}
            {error && (
                <div className="error-container">
                    <p>{error}</p>
                </div>
            )}
        </div>
    );
}

export default App;

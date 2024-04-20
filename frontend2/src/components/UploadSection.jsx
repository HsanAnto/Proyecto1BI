import React, { useState } from 'react';

const UploadSection = ({ setUploadedFile }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files && e.target.files[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  const handleUpload = () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData
      }).then(response => {
        if (response.ok) {
          alert('File uploaded successfully');
          setSelectedFile(null);
          setUploadedFile(true);
        } else {
          alert('Failed to upload file');
        }

      }).catch(error => {
        console.error(error);
        alert('Failed to upload file');
      });
    }
  };

  return (
    <div className="p-4 bg-white shadow-md rounded-md">
      <h2 className="text-xl font-semibold mb-4">Upload CSV File</h2>
      <input
        type="file"
        accept=".csv"
        className="hidden"
        id="csv-upload"
        onChange={handleFileChange}
      />
      <label
        htmlFor="csv-upload"
        className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded cursor-pointer inline-block"
      >
        Choose CSV File
      </label>
      {selectedFile && (
        <div className="mt-4">
          <p className="text-gray-600">Selected file: {selectedFile.name}</p>
          <button
            className="bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded mt-2"
            onClick={handleUpload}
          >
            Upload
          </button>
        </div>
      )}
    </div>
  );
};

export default UploadSection;

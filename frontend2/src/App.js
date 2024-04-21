import React, { useEffect, useState } from 'react';
import ReviewList from './components/ReviewList';
import UploadSection from './components/UploadSection';
import SingleReviewRating from './components/SingleReviewRating';

const App = () => {
  const [reviews, setReviews] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [uploadedFile, setUploadedFile] = useState(false);
  const [predicted, setPredicted] = useState(false);
  const [isPredicting, setIsPredicting] = useState(false);

  const clases = {
    clase1: ['cucarachas', 'nunca', 'peor', 'pesimo', 'no', 'pesima', 'mala', 'sucio', 'mal', 'horrible'],
    clase2: ['caro', 'parecia', 'llego', 'viejo', 'agua', 'ser', 'desear', 'mal', 'mala', 'no'],
    clase3: ['normal', 'mejorar', 'informacion', 'embargo', 'falta', 'creo', 'demasiado', 'bastante', 'parecio', 'regular'],
    clase4: ['comodas', 'bueno', 'duda', 'buen', 'buena', 'buenos', 'muy', 'agradable', 'excelente'],
    clase5: ['atencion', 'duda', 'gran', 'increible', 'excelente', 'gracias', 'encanto', 'super', 'deliciosa', 'ambiente']
  };

  const handlePredict = () => {
    setIsPredicting(true);
    // Fetch request to predict endpoint
    fetch('http://127.0.0.1:8000/predict/')
      .then(response => {
        // Handle response as needed
        if (response.ok) {
          alert("Prediction successful");
          setPredicted(true);
          setIsPredicting(false);
          fetchReviews(); // Fetch reviews after successful prediction
        } else {
          console.error("Prediction failed");
        }
      })
      .catch(error => {
        console.error("Prediction failed:", error);
      });
  };

  const fetchReviews = () => {
    setIsLoading(true);
    fetch('http://127.0.0.1:8000/reviews/')
      .then(response => response.json())
      .then(data => {
        const datos = JSON.parse(data);
        let reviews = [];
        for (let i = 0; i < datos.length; i++) {
          let words = datos[i].words;
          let clase = datos[i].Class;
          let wordsFiltered = [...new Set(words.filter(word => clases['clase' + clase].includes(word)))];
          let review = {
            Review: datos[i].Review,
            Class: clase,
            words: wordsFiltered
          };
          reviews.push(review);
        }
        setReviews(reviews);
        setIsLoading(false);
      })
      .catch(error => {
        console.error(error);
        setIsLoading(false);
      });
  };

  return (
    <div className="container mx-auto p-4">
      {!uploadedFile ? (
        <UploadSection setUploadedFile={setUploadedFile} />
      ) : (
        <div>
          <p className="bg-green-100 text-green-800 p-4 rounded-md mb-4">File uploaded successfully</p>
          <button
            className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded inline-block"
            onClick={() => setUploadedFile(false)}
          >
            Upload Another File
          </button>
          <button
            className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded ml-2 inline-block"
            onClick={handlePredict} // Call handlePredict when Predict button is clicked
          >
            Predict
          </button>
        </div>
      )}
      {isPredicting && <p>Predicting...</p>}
      <SingleReviewRating />
      {uploadedFile && predicted && (isLoading ? <p>Loading...</p> : <ReviewList reviews={reviews} />)}
    </div>
  );
};

export default App;
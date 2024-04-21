import React, { useState } from 'react';

const ReviewForm = () => {
  const [review, setReview] = useState('');
  const [predictedRating, setPredictedRating] = useState(null);

  const handleReviewChange = (event) => {
    setReview(event.target.value);
  };


  const handleSubmit = () => {
    if (review.trim() !== '') {
      const data = { review: review };
      fetch('http://127.0.0.1:8000/predict/single/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => {
          setPredictedRating(data);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  };

  return (
    <div className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h3 className="text-md">Write a Review:</h3>
        <textarea
          className="w-full h-32 p-2 border border-gray-300 rounded-md"
          value={review}
          onChange={handleReviewChange}
        ></textarea>
         {predictedRating !== null && (
          <p className="mt-2">Predicted Rating: {predictedRating}</p>
        )}
        <div className="rating">
          {Array.from({ length: 5 }).map((_, i) => (
            <input
              key={i}
              type="radio"
              name="rating"
              value={i + 1}
              className="mask mask-star-2 bg-orange-400 pointer-events-none"
              checked={predictedRating === i + 1}
              readOnly
            />
          ))}
        </div>
        <button
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded mt-2"
          onClick={handleSubmit}
        >
          Submit Review
        </button>
       
      </div>
    </div>
  );
};

export default ReviewForm;
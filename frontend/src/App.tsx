// src/App.tsx

import React from 'react';
import ReviewList from './components/ReviewList';

const App: React.FC = () => {
  const reviews = [
    { id: 1, text: "Great service!", stars: 5 },
    { id: 2, text: "Good food, but slow service.", stars: 4 },
    { id: 3, text: "Not worth it.", stars: 1 },
    // Add more reviews as needed
  ];

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Reviews</h1>
      <ReviewList reviews={reviews} />
    </div>
  );
}

export default App;

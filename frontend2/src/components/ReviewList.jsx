import React from 'react';

const ReviewList = ({ reviews }) => {
  return (
    <div className="space-y-4 flex flex-wrap gap-5">

      {reviews.length > 0 ? (
        reviews.map((review, index) => (
          <div key={index} className="card w-96 bg-base-100 shadow-xl">
            <div className="card-body">
              <h3 className="text-md">{review.Review}</h3>
              {review.words.length > 0 && <h3 className="font-bold text-lg">Palabras clave:</h3>}
                <p className="text-sm text-gray-500">
                    {review.words.join(", ")}
                </p>
              <div className="rating">
                {Array.from({ length: 5 }).map((_,i) => (
                  <input
                    key={i}
                    type="radio"
                    name={"rating-" + index}
                    className="mask mask-star-2 bg-orange-400 pointer-events-none"
                    checked={review.Class === i + 1}
                  />
                ))}
              </div>
            </div>
          </div>
        ))
      ) : (
        <p>No reviews found.</p>
      )}
    </div>
  );
};

export default ReviewList;

import React from 'react';

interface Review {
  id: number;
  text: string;
  stars: number;
}

interface Props {
  reviews: Review[];
}

const ReviewList: React.FC<Props> = ({ reviews }) => {
return (

    
    <div className="space-y-4">
        {reviews.map(review => (
            <div className="card w-96 bg-base-100 shadow-xl">
                <div className="card-body">
                    <h3 className="font-bold text-lg">{review.text}</h3>
                    <div className="rating">
                        <input type="radio" name={"rating-"+review.id} className="mask mask-star-2 bg-orange-400 pointer-events-none" checked={review.stars === 1} />
                        <input type="radio" name={"rating-"+review.id} className="mask mask-star-2 bg-orange-400 pointer-events-none" checked={review.stars === 2} />
                        <input type="radio" name={"rating-"+review.id} className="mask mask-star-2 bg-orange-400 pointer-events-none" checked={review.stars === 3} />
                        <input type="radio" name={"rating-"+review.id} className="mask mask-star-2 bg-orange-400 pointer-events-none" checked={review.stars === 4} />
                        <input type="radio" name={"rating-"+review.id} className="mask mask-star-2 bg-orange-400 pointer-events-none" checked={review.stars === 5} />
                    </div>
                </div>
            </div>
        ))}
    </div>
);
};

export default ReviewList;

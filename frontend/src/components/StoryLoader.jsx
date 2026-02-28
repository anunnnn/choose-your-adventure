import React, {
    useState,
    useEffect,
    useParams,
    useNavigate
} from 'react';
import axios from 'axios';

import LoadingStatus from './LoadingStatus';
import StoryGame from './StoryGame';

const API_BASE_URL = '/api';

export default function StoryLoader() {

    const {id} = useParams();
    const navigate = useNavigate();
    const [loading, setLoading] = useState(true);
    const [story, setStory] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() =>{
        loadStory(id)
    }, [id]);

    const loadStory = async (storyId) => {
        setLoading(true);
        setError(null);

        try {
            const response = await axios.get(`$(API_BASE_URL)/stories/${storyId}/complete`);
            setStory(response.data);
            setLoading(false);
        } catch (error){
            if(error.response?.status === 404){
                setError('Story not found');
            } else {
                setError('Failed to Load story');
            }
        } finally {
            setLoading(false);
        }
    }

    const createNewStory = () => {
        navigate('/');
    }

    if(loading){
        return (
            <LoadingStatus theme={theme} />
        );
    }

    if(error){
        return (
            <div className="story-loader">
                <div className="error-message">
                    <h2>Story Not Found</h2>
                    <p>{error}</p>
                    <button onClick={createNewStory}>Go to Story Generator </button>
                </div>
            </div>
        );
    }

    if(story){
        return (
            <div className="story-loader">
                <StoryGame story={story} onNewStory={createNewStory} />
            </div>
        );
    }
}

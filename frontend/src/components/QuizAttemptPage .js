import * as React from 'react';
import { ApiClient } from '../utils';
import Box from '@mui/material/Box';
import { useParams } from 'react-router-dom'

import QuizScreen from './QuizScreen';


const QuizAttemptPage = (props) => {
    const [questions, setQuestions ] = React.useState(null);
    const [creator, setCreator] = React.useState('');
    const { link } = useParams();
    
    React.useEffect(() => {
        async function getQuestions(){
            const response = await ApiClient.get(`/quiz/${link}`)
            setQuestions(response.data.questions);
            setCreator(response.data.creator);
        }
        getQuestions();
    }, [link]);

    if (!questions) return 'No questions found in this quiz!'

    return (
        <Box
            sx={{
                display: 'flex',
                flexWrap: 'wrap',
                '& > :not(style)': {
                m: 1,
                width: 500,
                height: 350,
                },
            }}
        >
            {
                <QuizScreen questions={questions} mode='attempt' link={link} creator={creator} />
            }

        </Box>
        
    );
}

export default QuizAttemptPage;

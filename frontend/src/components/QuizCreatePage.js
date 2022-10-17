import * as React from 'react';
import { ApiClient } from '../utils';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import QuizScreen from './QuizScreen';


const QuizCreatePage = (props) => {
    const [ questions, setQuestions ] = React.useState(null);
    const [ creator, setCreator ] = React.useState('');
    const [ startQuiz, setStartQuiz ] = React.useState(false);
    const [ nextButtonDisabled, setNextButtonDisabled ] = React.useState(true);
    
    React.useEffect(() => {
        async function getQuestions(){
            const response = await ApiClient.get('/questions');
            if(response.data.length)
                setQuestions(response.data);
        }
        getQuestions();
    }, []);

    const handNameChange = (e) => {
        setCreator(e.target.value);
        if(e.target.value !== ''){
            setNextButtonDisabled(false);
        }else{
            setNextButtonDisabled(true);
        }
    }

    if (!questions) return 'There are no questions to display right now'

    return (
        <>
        {
            startQuiz === true ?
            <QuizScreen questions={questions} mode='create' creator={creator} />
            :   <>
                    <TextField onChange={handNameChange} label="Enter your name" variant="standard" />
                    <ButtonGroup variant="contained" aria-label="outlined primary button group">
                        <Button disabled={nextButtonDisabled} onClick={() => setStartQuiz(true) }>Next</Button>
                    </ButtonGroup>
                </>
        }
        </>  
    );
}

export default QuizCreatePage;

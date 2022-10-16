import * as React from 'react';
import Question from './Question';
import { ApiClient } from '../utils';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import { Card } from '@mui/material';


const QuizScreen = (props) => {
    const [questionIndex, setQuestionIndex] = React.useState(0)
    const [disabledPrevious, setPreviousDisabled] = React.useState(true);
    const [nextButtonLabel, setNextButtonLabel ] = React.useState('Next');
    const [ quizLink, setQuizLink ] =  React.useState('');
    const [ quizDone, setQuizDone ] = React.useState(false);
    const [ quizSummary, setQuizSummary ] = React.useState({});

    // keeps a hold of all seletions user made in the questions
    const selections = React.useRef({})

    const { questions, mode, creator, link } = props;
    const question = questions[questionIndex];
    const questionCount = questions.length

    React.useEffect(() => {
        if (questionIndex - 1 < 0){
            setPreviousDisabled(true);
        }else{
            setPreviousDisabled(false);
        }

        if (questionIndex + 1 === questionCount){
            setNextButtonLabel('Submit');
        }else{
            setNextButtonLabel('Next');
        }

    }, [questionIndex, questionCount]);

    async function createQuiz(){
        const data = {
            creator,
            questions: selections.current
        }
        const response = await ApiClient.post('/quiz', data);
        const link = `http://localhost:3000/quiz/${response.data.quiz_link}`

        setQuizLink(link);
        setQuizDone(true);
    }

    async function checkAnswers(){
        const response = await ApiClient.post(`/quiz/${link}/check`, {answers: selections.current});
        setQuizSummary(response.data);
        setQuizDone(true);
    }

    const loadQuestion = (fwd) => {
        if(fwd === true){
            // if reached at last question then
            // either create quiz or check results
            if (questionIndex + 1 === questionCount){
                if(mode === 'create'){
                    createQuiz();
                } else {
                    checkAnswers();
                }
            } else{
                setQuestionIndex(questionIndex + 1)
            }
        } else{
           setQuestionIndex(questionIndex - 1)
        }
    };

    return (
        <Card>
            {
                quizDone === true ?
                    mode === 'create' ?
                    <h3>Link { quizLink }</h3>
                    :
                    <h3>You know {creator} - {quizSummary.percentage}% </h3>
                :   <>
                        <Question {...question} selections={selections} />
                        <ButtonGroup variant="contained" aria-label="outlined primary button group">
                            <Button disabled={disabledPrevious} onClick={() => loadQuestion(false)}>Previous</Button>
                            <Button onClick={() => loadQuestion(true)}>{nextButtonLabel}</Button>
                        </ButtonGroup>
                    </>
            }
        </Card>
    );
}

export default QuizScreen;

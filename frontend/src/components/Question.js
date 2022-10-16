import * as React from 'react';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Choice from './Choice';


const Question = (props) => {
    const questionText = props.question_text; 
    const { id, choices, selections } = props;

    // this question's selections
    const selectedOptions = selections.current[id] || [];
    
    return (
        <>
            <CardContent>
                <Typography variant="h5" component="div">
                    {questionText}
                </Typography>
                {
                    choices.map((choice) => {
                        let selected = selectedOptions.indexOf(choice.id) !== -1 ? true : false;
                        return <Choice 
                            key={choice.id} 
                            id={choice.id} 
                            questionId={id}
                            text={choice.choice_text}
                            selected={selected}
                            selections={props.selections}
                        />
                    })
                }
            </CardContent>
        </>
    );
}


export default Question;

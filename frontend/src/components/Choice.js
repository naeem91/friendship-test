import * as React from 'react';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';


const Choice = (props) => {
    const [checked, setChecked] = React.useState(props.selected);
    const choiceID = props.id;
    const questionId = props.questionId;
    let currentChoices = props.selections.current[questionId] || [];
    
    React.useEffect(() => {
        if(checked === true){
            currentChoices.push(choiceID);
        }else{
            currentChoices.pop(choiceID);
        }
        props.selections.current[questionId] = [...new Set(currentChoices)];
    }, [checked]);

    const handleChange = (event) => {
        setChecked(event.target.checked);
    };

    return (
        <FormGroup>
            <FormControlLabel 
                control={<Checkbox checked={checked} onChange={handleChange} />} 
                label={props.text} 
            />
        </FormGroup>
    )
}


export default Choice;

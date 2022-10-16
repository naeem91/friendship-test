import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import QuizCreatePage from './components/QuizCreatePage';
import QuizAttemptPage from './components/QuizAttemptPage ';


function App() {
  return (
    <Router>
      <React.Fragment>
        <CssBaseline />
            <Card sx={{
              width: 600,
              height: 400,
              margin: '10px auto',
              border: '1px dotted',
              padding: '10px'
            }}>
              <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                Friendship Test!
               </Typography> 
              <Routes>
                <Route path='/' element={ <QuizCreatePage /> } />
                <Route path='/create' element={ <QuizCreatePage /> } />
                <Route path='/quiz/:link' element={ <QuizAttemptPage /> } />
              </Routes>
            </Card>
      </React.Fragment>
    </Router>
  );
}

export default App;

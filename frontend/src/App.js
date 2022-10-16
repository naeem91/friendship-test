import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';

import QuizCreatePage from './components/QuizCreatePage';
import QuizAttemptPage from './components/QuizAttemptPage ';


function App() {
  return (
    <Router>
      <React.Fragment>
        <CssBaseline />
        <Container maxWidth="sm">
            <Routes>
              <Route path='/' element={ <QuizCreatePage /> } />
              <Route path='/create' element={ <QuizCreatePage /> } />
              <Route path='/quiz/:link' element={ <QuizAttemptPage /> } />
            </Routes>
        </Container>
      </React.Fragment>
    </Router>
  );
}

export default App;

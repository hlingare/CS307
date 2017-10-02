import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import CourseListView from './Components/CourseListView';
import Callback from './Components/Callback';
import { Router, Route,Switch } from 'react-router';
import { BrowserRouter } from 'react-router-dom'

const Root = () => {
  return (
   <BrowserRouter>
     <Switch>
        <Route exact path="/" component={App}/>
        <Route path="/courses" component={CourseListView}/>
     </Switch>
    </BrowserRouter>
  )
}

ReactDOM.render(<Root />, document.getElementById('root'));
registerServiceWorker();

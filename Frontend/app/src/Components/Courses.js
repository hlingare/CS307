import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { getCourseDescription } from '../utils/api';
import ReactDisqusComments from 'react-disqus-comments';


import history from '../history';
import '../styles/nav.css';

class Courses extends Component {

  constructor() {
    super()
    this.state = {
      courseDescription: '',
      name: '',
      timings:'',
      professor: '',
    };
  }

  componentDidMount() {
    this.getCourseDescription();

  }

  handleNewComment(comment){
		console.log(comment.text);
	}
  getCourseDescription() {
    getCourseDescription(this.props.location.state.detail).then((courseDescription) => {
      this.setState({
        courseDescription: courseDescription.result.description,
        name: courseDescription.result.name,
        timings: courseDescription.result.timings,
        professor: courseDescription.result.professor,
      });
    });

  }

  render() {
    return (
      <div>
      <span>{this.state.courseDescription}</span>
      <span>{this.state.name}</span>
      <span>{this.state.professor}</span>
      <span>{this.state.timings}</span>
      <ReactDisqusComments
  				shortname="courserec"
  				identifier={this.state.name}
  				title={this.state.name}
  				onNewComment={this.handleNewComment}
     />

      </div>

    );
  }
}

export default Courses;

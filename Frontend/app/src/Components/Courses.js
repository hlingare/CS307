import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { getCourseDescription } from '../utils/api';

import history from '../history';
import '../styles/nav.css';
import '../styles/CourseSpec.css';


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
      <div className="coursePeck">

      <div className="container">
        <h3 className="text-center">{this.state.name}</h3>
      </div>

      <div>
        <br />
        <center><label>Course Description: </label></center>
        <label  >{this.state.courseDescription}</label>
        <br />
        <label>{this.state.professor}</label>
        <br />
        <label>{this.state.timings}</label>
        <br />
        <label>{this.state.name}</label>
        <br />
      </div>







      </div>





    );
  }
}

export default Courses;

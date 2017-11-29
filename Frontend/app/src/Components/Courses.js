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

  myFunction1() {
    //console.log("why am im going in here at start");
    var email = this.state.name.toUpperCase()
    var courseinfo = this.state.courseDescription;
        window.location.href = "mailto:" + "" + "?subject=" + "Course Information of "+email+"&body="+"CourseInfo: "+courseinfo+"%0A"+"%0A"+"Course Timing: "+this.state.timings+"%0A"+"%0A"+"Professor Name: "+this.state.professor;
  }

  render() {
    return (
      <div className="form1">

      <div className="container">
        <h3 className="text-center">{this.state.name.toUpperCase()}</h3>
        <button onClick={this.myFunction1.bind(this,"")}>Click me</button>
      </div>

      <div>
        <br/>
        <h4><label className="label2" >Course Description: </label></h4>
        <label className="label1" >{this.state.courseDescription}</label>
        <br/>
        <h4><label className="label2" >Professor: </label></h4>
        <label className="label1">{this.state.professor}</label>
        <br/>
        <h4><label className="label2" >Course Timings: </label></h4>
        <label className="label1">{this.state.timings}</label>
        <h4><label className="label2" >Average Grade: </label></h4>
        <label className="label1">A</label>
      </div>







      </div>





    );
  }
}

export default Courses;

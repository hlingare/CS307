import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { getCourseDescription } from '../utils/api';
import ReactDisqusComments from 'react-disqus-comments';
import '../styles/CourseSpec.css';

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
      grade: '',
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
      console.log(courseDescription.result);
      this.setState({
        courseDescription: courseDescription.result.description,
        name: courseDescription.result.name,
        timings: courseDescription.result.timings,
        professor: courseDescription.result.professor,
        grade: courseDescription.result.grade,
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
      <div>

      <div className="container">
        <h3 className="text-center">{this.state.name.toUpperCase()}</h3>
        <button className="button" onClick={this.myFunction1.bind(this,"")}>Share</button>
      </div>

      <div className="container1">
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
        <label className="label1">{this.state.grade}</label>
        <h4><label className="label2" >Predicted Grade: </label></h4>
        <label className="label1">{this.state.grade}</label>
      </div>
      </div>
      <ReactDisqusComments
          style={{padding: "30px"}}
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

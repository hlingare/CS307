<<<<<<< HEAD
import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
<<<<<<< HEAD
import '../styles/courseList.css';
import { getCourseData } from '../utils/api';

=======
import { getCourseData } from '../utils/courselist-api';
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196

class CourseListView extends Component {

  constructor() {
    super()
<<<<<<< HEAD
    this.state = { courses: [] };
  }

  getCourseData() {
  getCourseData().then((courses) => {
    this.setState({ courses });
  });
}

componentDidMount() {
  this.getCourseData();
}

  render() {
    const { courses }  = this.state;
    console.log(courses);

    return (
    <div>
      <div className="container">
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
          </div>
          <div className="list">
        { courses.map((course, index) => (
              <div className="courseName" key={course.id}>
              <span>{course.title}</span>
              <span className="recommend">{'RECOMMENDED'}</span>
              </div>
          ))}
          </div>
          </div>
=======
    this.state = { courses: [] }; 
}


  getCourseList() {
	getCourseData().then((courses) => {
		this.setState({ courses });
		console.log( courses );
	});
  }

  componentDidMount() {
	this.getCourseList();
  }

  render() {
    const { courses }  = this.state;

    return (
      <div>
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
        <hr/>

        { courses.map((course, index) => (
              <div className="col-sm-6" key={index}>
		<div className="panel panel-danger">
		<div className="panel-heading">
		<h3 className="panel-title"><span className="btn">#{ course.id }</span></h3>
              </div>
		<div className="panel-body">
		 <p> { course.course } </p>
		</div>
		</div>
		</div>
          ))}
          </div>
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196
    );
  }
}

export default CourseListView;
=======
import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
import '../styles/courseList.css';
import { getCourseData } from '../utils/api';
import history from '../history';


class CourseListView extends Component {

  constructor() {
    super()
    this.state = { courses: [] };
  }

  getCourseData() {
  getCourseData().then((courses) => {
    this.setState({ courses });
  });
}

componentDidMount() {
  this.getCourseData();
}

listcourse() {
  history.push('/listcourse');
}

  render() {
    const { courses }  = this.state;
    console.log(courses);

    return (
    <div>
      <div className="container">
        <Nav auth={this.auth} {...this.props}  />
        <h3 className="text-center">Courses</h3>
          </div>
          <div className="list">
        { courses.map((course, index) => (
              <div className="courseName" key={course.id} onClick={this.listcourse}>
              <span>{course.title}</span>
              <span className="recommend">{'RECOMMENDED'}</span>
              </div>
          ))}
          </div>
          </div>
    );
  }
}

export default CourseListView;
>>>>>>> 7a1d3ccb336b322fc03ebd46134d5d9af4150a20

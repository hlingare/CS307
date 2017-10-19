import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
import '../styles/courseList.css';
import { getCourseData } from '../utils/api';


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
    );
  }
}

export default CourseListView;

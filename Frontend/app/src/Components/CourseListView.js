import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
import '../styles/courseList.css';
import { getCourseData } from '../utils/api';
import history from '../history';
import Courses from './Courses';


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

listcourse(title) {
 history.push({
  pathname: '/listcourse',
  state: { detail: title }
})
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
              <div className="courseName" key={course.id} onClick={() => this.listcourse(course.title)}>
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
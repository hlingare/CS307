import React, { Component } from 'react';
import { Link } from 'react-router';
import Nav from './Nav';
//import axios from 'axios';


class CourseListView extends Component {

  constructor() {
    super()
    this.state = { courses: ['EAPS100'] }; 
}

//ajax request
 componentWillMount() {
	var self = this;
	fetch('https://localhost:3000/testinp.txt')
	.then(function(response) {
		if() {
		} else {
		}	
	})
	.then(function(body) {
		self.setState({
			courses: JSON.parse(body).courselist
		});
	});
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
              {course}
              </div>
          ))}
          </div>
    );
  }
}

export default CourseListView;

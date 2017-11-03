import axios from 'axios';

export {getCourseData,postUserData,postCourseData,getUserData,getCourseDescription};

function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}

function postUserData(userIdAuth0,name) {
 const url = `https://courserec.herokuapp.com/showStudent`;
  axios.post(url, {
      userId: userIdAuth0,
      name: name
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

function postCourseData(userIdAuth0,Coursename,performance) {
 const url = `https://courserec.herokuapp.com/showCourse`;
  axios.post(url, {
      userId: userIdAuth0,
      course_name: Coursename,
      option: performance
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

function getUserData() {
  var uid = window.localStorage.getItem("uid");
  const url = `https://courserec.herokuapp.com/getUserName`;
  console.log(uid)
  return axios.get(url, {
    params: {
      uid: uid
    }
  }).then(response => response.data);
}

function postUserName(userIdAuth0,userName) {
	const url = `https://courserec.herokuapp.com/updateUsername`;
		axios.post(url, {
			userId: userIdAuth0,
			username: userName
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

function getCourseDescription(courseName) {
  console.log("description")
  const url = `https://courserec.herokuapp.com/getCourse`;
  return axios.get(url, {
    params: {
      coursename: courseName
    }
  }).then(response => response.data);
}
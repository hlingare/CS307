import axios from 'axios';

export {
  getCourseData,
  postUserData,
  postUserName,
  postCourseData,
  getUserData,
  getCourseDescription,
  postVote,
  postUserName,
  getVote
};

function getCourseData() {
  var uid = window.localStorage.getItem("uid");
  const url = `https://courserec.herokuapp.com/get_result_list`;
  return axios.get(url,{
    params: {
      userId: uid
    }}).then(response => response.data);
}
function postUserData(userIdAuth0,name) {
  console.log(userIdAuth0);
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

function postCourseData(userIdAuth0,Coursename,Number1) {
 const url = `https://courserec.herokuapp.com/showCourse`;
  axios.post(url, {
      userId: userIdAuth0,
      course_name: Coursename,
      option: Number1
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
  console.log("Post ")
  console.log(userName)
	const url = `https://courserec.herokuapp.com/updateUsername`;
		axios.post(url, {
			userId: userIdAuth0,
			name: userName
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

function getCourseDescription(courseName) {
  const url = `https://courserec.herokuapp.com/getCourse`;
  return axios.get(url, {
    params: {
      coursename: courseName
    }
  }).then(response => response.data);
}

function postVote(title,votes) {
	const url = `https://courserec.herokuapp.com/postVote`;
		axios.post(url, {
			courseName: title,
			upvote: votes
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

function getVote(courseName) {
  const url = `https://courserec.herokuapp.com/getVote`;
  return axios.get(url, {
    params: {
      courseName: courseName
    }
  }).then(response => response.data);
}

import axios from 'axios';

export {getCourseData, getProfileData, postUserData};

function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}

function getProfileData(userIdAuth0) {
	//TODO: update url
	const url = `https://courserec.herokuapp.com/getUserName/` + userIdAuth0;
	return axios.get(url).then(response => response.data);
}

function postUserData(userIdAuth0, courseName) {
 const url = `https://courserec.herokuapp.com/showStudent/` + userIdAuth0 + `,` + courseName;

  axios.post(url, {
      userId: userIdAuth0,
      cname: courseName
})
.then(function (response) {
console.log(response);
})
.catch(function (error) {
console.log(error);
});
}

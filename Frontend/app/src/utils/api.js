import axios from 'axios';

export {getCourseData};


function getCourseData() {
  const url = `https://courserec.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}

function getProfileData() {
	const url = `https://courserec.herokuapp.com/prereg`;
	  return axios.get(url).then(response => response.data);
}



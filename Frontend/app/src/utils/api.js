import axios from 'axios';

export {getCourseData};

function getCourseData() {
  const url = `https://gentle-coast-95666.herokuapp.com/prereg`;
  return axios.get(url).then(response => response.data);
}

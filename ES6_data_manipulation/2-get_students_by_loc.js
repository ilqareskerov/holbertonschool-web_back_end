function getStudentsByLocation(students, city) {
    // returns desired student by location
    return students.filter((student) => student.location === city);
  }
  
  export default getStudentsByLocation;
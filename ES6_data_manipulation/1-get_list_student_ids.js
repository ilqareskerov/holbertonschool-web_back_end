function getListStudentIds(studentArray) {
    // Check if the argument is an array
    if (!Array.isArray(studentArray)) {
      return [];
    }
  
    // Use map to extract ids from each student object
    return studentArray.map((student) => student.id);
  }
  
  export default getListStudentIds;

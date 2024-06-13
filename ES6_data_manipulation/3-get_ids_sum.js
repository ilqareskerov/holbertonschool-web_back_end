function getStudentIdsSum(students) {
    // returns sum of the ids
    return students.reduce((sum, student) => sum + student.id, 0);
  }
  
  export default getStudentIdsSum;
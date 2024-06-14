import getListStudents from "./0-get_list_students";

function getListStudentIds () {
  if (!Array.isArray(students)){
    return [];
  }

  const ids = students.map((item) => item.id);

  return ids;
}

export default getListStudentIds;

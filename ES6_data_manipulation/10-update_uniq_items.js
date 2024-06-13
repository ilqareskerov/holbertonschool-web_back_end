function updateUniqueItems(map) {
    if (!(map instanceof Map)) {
      throw new TypeError('Cannot process: Argument must be a Map');
    }
    for (const [item, quantity] of map) {
      if (quantity === 1) {
        map.set(item, 100);
      }
    }
    return map;
  }
  
  export default updateUniqueItems;

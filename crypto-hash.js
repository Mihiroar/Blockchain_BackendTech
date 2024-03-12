const crypto = require('crypto');
const cryptoHash = (...inputs) => {
  const hash = crypto.createHash("sha256");
  hash.update(inputs.sort().join(''));
  return hash.digest('hex');
};

// result = cryptoHash("hello", "world", "!"); //The generated hash is of concatenation of the hello , world & !
// console.log(result);

module.exports = cryptoHash;
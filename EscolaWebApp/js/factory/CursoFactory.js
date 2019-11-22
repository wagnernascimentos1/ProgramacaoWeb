// Curso - Factory
var cursoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/cursos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/cursos/" + encodeURI(id))
  };

  var _cadastrar = function(curso) {
    return $http.post(baseUrl + "/curso", curso)
  };

  var _atualizar = function(curso) {
    return $http.put(baseUrl+ "/curso/" + encodeURI(id), curso)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("cursoApi", cursoFactory);

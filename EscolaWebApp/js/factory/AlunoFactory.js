/ Aluno - Factory
var alunoFactory = function($http) {

  var baseUrl = "localhost:5000";

  var _listar = function() {
    return $http.get(_baseUrl+ "/alunos")
  };

  var _buscarPorId = function(id) {
    return $http.get(_baseUrl+ "/alunos/" + encodeURI(id))
  };

  var _cadastrar = function(aluno) {
    return $http.post(baseUrl + "/aluno", aluno)
  };

  var _atualizar = function(aluno) {
    return $http.put(baseUrl+ "/aluno/" + encodeURI(id), aluno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("alunoApi", alunoFactory);

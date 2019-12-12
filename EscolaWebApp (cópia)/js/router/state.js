/**
 * Configuração da rota com ui-router.
 */
app.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

    // Rota padrão.
    $urlRouterProvider.otherwise("/home");

    // Estados
    $stateProvider
      // Home
      .state('home', {
        url: '/home',
        title: 'EscolaApp - Página Principal',
        templateUrl: 'home.html',
        controller: 'HomeController'
      })
      .state('aluno', {
        url: '/aluno',
        title: 'EscolaApp - Cadastrar Aluno',
        templateUrl: 'aluno.html',
        controller: 'AlunoController'
      })
      .state('alunos', {
        url: '/alunos',
        title: 'EscolaApp - Listar Alunos',
        templateUrl: 'alunos.html',
        controller: 'AlunosController'
      })
      .state('campus', {
        url: '/campus',
        title: 'EscolaApp - Cadastrar Campus',
        templateUrl: 'campus.html',
        controller: 'CampusController'
      })
      .state('campi', {
        url: '/campi',
        title: 'EscolaApp - Listar Campi',
        templateUrl: 'campi.html',
        controller: 'CampiController'
      })
      .state('curso', {
        url: '/curso',
        title: 'EscolaApp - Cadastrar Curso',
        templateUrl: 'curso.html',
        controller: 'CursoController'
      })
      .state('cursos', {
        url: '/cursos',
        title: 'EscolaApp - Listar Cursos',
        templateUrl: 'cursos.html',
        controller: 'CursosController'
      })
      .state('disciplina', {
        url: '/disciplina',
        title: 'EscolaApp - Cadastrar Disciplina',
        templateUrl: 'disciplina.html',
        controller: 'DisciplinaController'
      })
      .state('disciplinas', {
        url: '/disciplinas',
        title: 'EscolaApp - Listar Disciplinas',
        templateUrl: 'disciplinas.html',
        controller: 'DisciplinasController'
      })
      .state('endereco', {
        url: '/endereco',
        title: 'EscolaApp - Cadastrar Endereco',
        templateUrl: 'endereco.html',
        controller: 'EnderecoController'
      })
      .state('enderecos', {
        url: '/enderecos',
        title: 'EscolaApp - Listar Enderecos',
        templateUrl: 'enderecos.html',
        controller: 'EnderecosController'
      })
      .state('escola', {
        url: '/escola',
        title: 'EscolaApp - Cadastrar Escola',
        templateUrl: 'escola.html',
        controller: 'EscolaController'
      })
      .state('escolas', {
        url: '/escolas',
        title: 'EscolaApp - Listar Escolas',
        templateUrl: 'escolas.html',
        controller: 'EscolasController'
      })
      .state('professor', {
        url: '/professor',
        title: 'EscolaApp - Cadastrar Professor',
        templateUrl: 'professor.html',
        controller: 'ProfessorController'
      })
      .state('professores', {
        url: '/professores',
        title: 'EscolaApp - Listar Professores',
        templateUrl: 'professores.html',
        controller: 'ProfessoresController'
      })
      .state('turma', {
        url: '/turma',
        title: 'EscolaApp - Cadastrar Turma',
        templateUrl: 'turma.html',
        controller: 'TurmaController'
      })
      .state('turmas', {
        url: '/turmas',
        title: 'EscolaApp - Listar Turmas',
        templateUrl: 'turmas.html',
        controller: 'TurmasController'
      })
      .state('turno', {
        url: '/turno',
        title: 'EscolaApp - Cadastrar Turno',
        templateUrl: 'turno.html',
        controller: 'TurnoController'
      })
      .state('turnos', {
        url: '/turnos',
        title: 'EscolaApp - Listar Turnos',
        templateUrl: 'turnos.html',
        controller: 'TurnosController'
      })
  })
  //take all whitespace out of string
 .filter('nospace', function() {
   return function(value) {
     return (!value) ? '' : value.replace(/ /g, '');
   };
 })
 //replace uppercase to regular case
 .filter('humanizeDoc', function() {
   return function(doc) {
     if (!doc) return;
     if (doc.type === 'directive') {
       return doc.name.replace(/([A-Z])/g, function($1) {
         return '-' + $1.toLowerCase();
       });
     }

     return doc.label || doc.name;
   }
 });

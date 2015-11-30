'use strict';

module.exports = function(grunt) {

    // Carrega todos os plugins
    require('load-grunt-tasks')(grunt);
    // Cria estatísticas de tempo de build
    require('time-grunt')(grunt);

    grunt.initConfig({

        /* Configuração global do aplicativo.
            Aqui carregamos dados sobre a OA, bem como o objeto pkg.
        */
        app: {
            pkg: grunt.file.readJSON('package.json'),
            dev: 'HUBqueue/dev',
            temp: 'HUBqueue/temp',
            dist: 'HUBqueue/www',
            vendor: 'HUBqueue/dev/static/lib'
        },

        /* "Compilador" de javascript
            Faz a leitura do código e procura por erros estáticos.
        */
        jshint: {
            options: {
                jshintrc: true
            },

            defaults: [
                '<%= app.dev %>/static/controllers/*.js'
            ]
        },

        /* Injetor de dependências
            Insere tags no código relativas às dependências do projeto.
        */
        injector: {
            options: {
                addRootSlash: true,
                //min: true,
                bowerPrefix: 'bower',
                ignorePath: '<%= app.dev %>'
            },

            localDependencies: {
                files: {
                    '<%= app.dev %>/templates/Ground/index.html': [
                        // bootstrap usa less ao invés de css como padrão
                        '<%= app.vendor %>/bootstrap/dist/css/bootstrap.min.css',
                        '<%= app.dev %>/static/styles/*.css',
                        '<%= app.dev %>/static/app.js',
                        '<%= app.dev %>/static/controllers/*.js',
                        //'<%= app.dev %>/static/scripts/*.js'
                        '<%= app.dev %>/static/lib/angular-cookies/bower-angular-cookies-1.4.8/angular-cookies.js',
                        '<%= app.dev %>/static/lib/fullcalendar/dist/gcal.js'
                    ]
                }
            },

            bowerDependencies: {
                files: {
                    '<%= app.dev %>/templates/Ground/index.html': ['bower.json']
                }
            }
        },

        /* Limpa arquivos.
            Usaremos para limpar o www/ antes do build, e limpar o dev/ após.
        */
        clean: {
            preDist: [
                '<%= app.dist %>/*',
                '!<%= app.dist %>/.git'    
            ],

            postDist: [
                '<%= app.dev %>/*',
                '!<%= app.dev %>/.git'
            ]
        },

        /* Copia o conteúdo da pasta de desenvolvimento para de distribuição.
            Por hora, copiamos tudo, mas mais para frente, no desenvolvimento,
            vamos usar o copy para a minificação otimizada dos arquivos. */
        copy: {
            dist: {
                expand: true,
                cwd: '<%= app.dev %>',
                dest: '<%= app.dist %>',
                src: '**'
            }
        }

    });

    grunt.registerTask('install', [
        'injector'
    ]);

    /* Mais a frente no projeto, vamos fazer o build mais complexo, com
        minificação e afins */
    grunt.registerTask('build', [
        //'jshint', fazer o linting do javascript do Cláudio em outro momento
        'clean:preDist',
        'copy'
    ]);

};
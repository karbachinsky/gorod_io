module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
 
 
		compass: {
			dist: {
				options: {
					basePath:'../../gorod/static/gorod/',
					sassDir:'scss',
					cssDir:'css',
					imagesDir : 'img',
					httpPath : '/static/gorod/',
					outputStyle:'compressed',
					sourcemap: true
				}
			}
	 },
 
		watch: {
			compass: {
				files: '../../gorod/static/gorod/scss/*.scss', // следить за изменениями любых файлов с разширениями .scss
				tasks: ['compass'] // и запускать такую задачу при их изменении
			}
		}
 
	});
 
	//погружаем все необходимые модули
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-compass');
 
	//забиваем в задачу по умолчению все наши задачи
	grunt.registerTask('default', ['compass', 'watch']);
};
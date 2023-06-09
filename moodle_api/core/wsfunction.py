class WSFunction:

    def __init__(self):
        pass

    def descadastrar_curso(self, token, usuarioID, cursoID):
        descadastrar = {
            'wstoken': token,
            'wsfunction' : 'enrol_manual_unenrol_users',
            'enrolments[0][userid]' : usuarioID,
            'enrolments[0][courseid]' : cursoID,
            'enrolments[0][roleid]' : 5, #5 para aluno
            'moodlewsrestformat' : 'json'
        }

        return descadastrar
    
    def diciplinas_matriculadas(self, token, usuarioID):
        todas_disciplinas_matriculadas = {
            'wstoken': token,
            'wsfunction' : 'core_enrol_get_users_courses',
            'userid' : usuarioID,
            'moodlewsrestformat' : 'json'
        }

        return todas_disciplinas_matriculadas
    
    def cadastrar_curso(self, token, usuarioID, cursoID, timestamp_matricula, suspenso = 0):
        cadastrar = {
            'wstoken': token,
            'wsfunction' : 'enrol_manual_enrol_users',
            'enrolments[0][userid]' : usuarioID,
            'enrolments[0][courseid]' : cursoID,
            'enrolments[0][timestart]' : timestamp_matricula, #em milisenconds, data de inicio
            'enrolments[0][suspend]' : suspenso, # 1 é suspenso e 0 ativo.
            'enrolments[0][roleid]' : 5, #5 para aluno
            'moodlewsrestformat' : 'json'
        }

        return cadastrar
    
    def cadastrar_cohort(self, token, cohortID, usuarioID):
        cadastro_cohort = {
            'wstoken': token,
            'wsfunction' : 'core_cohort_add_cohort_members',
            'members[0][cohorttype][type]' : 'id',
            'members[0][cohorttype][value]' : cohortID,
            '&members[0][usertype][type]' : 'id',
            'members[0][usertype][value]' : usuarioID,
            'moodlewsrestformat' : 'json'
        }

        return cadastro_cohort
    

import numpy as np

A = np.ndarray

N_QUESTIONS = 32

def myers_briggs_score(question_logps):
    '''
    question_logps: [N_QUESTIONS, 5] array of logps for answers 1-5 (indices 0-4) for each question.
    '''

    expected_scores = []
    for i in range(question_logps.shape[0]):
        question_probs = np.exp(question_logps)
        expected_score = (question_probs[i] * np.array([1,2,3,4,5])).sum()
        expected_scores.append(expected_score)

    # zero indexes
    Q = ["Error"] + expected_scores

    # IE_scoring = '30 - Q3 - Q7 - Q11 + Q15 - Q19 + Q23 + Q27 - Q31'
    IE_score = 30  - Q[3] - Q[7] - Q[11] + Q[15] - Q[19] + Q[23] + Q[27] - Q[31]
    # SN_scoring = '12 + Q4 + Q8 + Q12 + Q16 + Q20 - Q24 - Q28 + Q32'
    SN_score = 12 + Q[4] + Q[8] + Q[12] + Q[16] + Q[20] - Q[24] - Q[28] + Q[32]
    # FT_scoring = '30 - Q2 + Q6 + Q10 - Q14 - Q18 + Q22 - Q26 - Q30'
    FT_score = 30 - Q[2] + Q[6] + Q[10] - Q[14] - Q[18] + Q[22] - Q[26] - Q[30]
    # JP_scoring = '18 + Q1 + Q5 - Q9 + Q13 - Q17 + Q21 - Q25 + Q29'
    JP_score = 18 + Q[1] + Q[5] - Q[9] + Q[13] - Q[17] + Q[21] - Q[25] + Q[29]

    print(
        '''
        If IE is more than 24, you are extroverted (E), otherwise you are introverted (I).
        If SN is more than 24, you are intuitive (N), otherwise you are sensing (S).
        If FT is more than 24, you are thinking (T), otherwise you are feeling (F).
        If JP is more than 24, you are perceiving (P), otherwise you are judging (J).
        Combine the four letters to get your personality type (e.g. I, S, F, P => ISFP).
        '''
    )

    print(f"IE_score: {IE_score}")
    print(f"SN_score: {SN_score}")
    print(f"FT_score: {FT_score}")
    print(f"JP_score: {JP_score}")

logps = -2 * np.random.rand(N_QUESTIONS, 5)

myers_briggs_score(logps)

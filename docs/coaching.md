# Coaching protocol

The [30-milestone map](milestones.md) is the common project-understanding target. [Watrous](learning.md) is the sole educational anchor; [worked bridges](learning-bridges.md) supply the missing project-specific connections. Explanations are provided in the conversation. This page specifies how to teach and assess that map; it is not a second curriculum or a learner's progress record.

## One milestone, one challenge

Every round contains **Revise → Learn → Test**. Revision supplies the definitions, notation, assumptions, and earlier results needed for the question. Learn explains the concept or repairs an identified misconception. A challenge attempt includes these blocks too, without revealing its answers.

All questions have four options and exactly one correct answer. They test inference, physical meaning, changed assumptions, resource accounting, or the interpretation of a result with minimal mental calculation. They should not require lengthy algebra or recall of prerequisites that were not supplied.

A new milestone starts with a compact Revise → Learn introduction and a **two-question challenge**. Every answer in the same challenge attempt must be correct to pass. Do not pool correct answers across failed attempts. A challenge's multi-question Test is one round, not one teaching round per question.

## Feedback and retries

The default challenge presentation is one question at a time, with correctness and explanations withheld until all questions in the attempt have been answered. Complete the challenge even after a wrong answer, then report the result. This avoids feedback on one question revealing a later answer.

After a failed challenge, conduct **1–3 targeted learning rounds**. Each round has Revise, Learn, and a one-question Test. Give correctness and an explanation immediately after each learning answer, including an incorrect answer in the last learning round. A learning-test error changes the teaching, not the challenge counter. Finish the bounded learning block, then retry the challenge with fresh applications.

If $f$ challenges have been completed unsuccessfully in the current milestone, the next challenge contains

$$
q=\min(2+f,6)
$$

questions. The sizes are 2, 3, 4, 5, 6, then 6 again as needed. Only a failed **challenge** increases $f$. Learning-test mistakes do not. A pass completes the milestone and the next milestone restarts at two questions. Do not count an interruption as a failure, increase the size beyond six, lower the passing threshold, or append an unlimited remedial loop within one learning phase.

The map's teaching-intensity field guides the 1–3-round block from the conceptual difficulty; the actual misconception determines the examples. More retry questions broaden conceptual evidence rather than increase computation. Replace an ambiguous, malformed, or unreadable item without penalizing the learner.

## Selection interface

Prefer genuine native answer buttons or selectable quiz controls when the current interface supports answer submission. During learning, show immediate feedback; during a challenge, use the full-attempt feedback rule above. Plain Markdown options, ordinary links, and expandable answer panels are not answer-submission controls. Do not label them as an interactive quiz.

When native selection is unavailable, state that limitation once and use the smallest selection-only fallback, such as one option letter. Do not require free-text explanations in place of the selected-answer protocol. Repository maintenance does not start a lesson or imply that any milestone has passed.

## Session state and endpoint

Keep session state separate from these public scientific files: map identifier, current milestone, passed milestone IDs, completed failed challenges in this milestone, current phase, question index, submitted answers, and targeted misconceptions. Preserve an unfinished challenge when resuming. A useful display is `M07 of 30 · challenge 2 · question 1 of 3`, not a fabricated estimate of competence.

The shortest route is 60 challenge questions if all initial attempts pass. Retries and learning rounds increase the total; there is no promised maximum under repeated failures. Do not infer passes from old tutorial answers, acceptance of a repository change, or repeated requests to continue.

Passing M01–M30 completes this project-understanding tutorial. State that completion explicitly. M14 integrates the background; M30 integrates the research. Do not add an unannounced final examination or reset passed milestones to prolong the course. Completion is evidence of the understanding tested here, not independent proof validation, mastery of every specialist detail, or guaranteed answers to every collaborator question.

from flask import Flask

from utils import load_json, all_candidates, format_candidates, get_candidate_by_id, candidates_by_skill
app = Flask(__name__)


@app.route('/')
def page_main():
    candidates: list[dict] = all_candidates()
    result: str = format_candidates(candidates)

    for candidate in candidates:
        result += f"""{candidate["name"]}\n
        {candidate["position"]}\n
        {candidate["skills"]}\n
        """
    result += "<pre>"
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    skill_lower = skill.lower
    candidates: list[dict] = candidates_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


if __name__ == "__main__":
    app.run(debug=True)

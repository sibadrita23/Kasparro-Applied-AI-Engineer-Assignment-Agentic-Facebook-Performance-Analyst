def test_eval():
    from src.agents.evaluator_agent import EvaluatorAgent
    hypos = [{"reason": "Test", "confidence": 0.65, "evidence": "Evidence", "summary": "Summary"}]
    evaluated = EvaluatorAgent().evaluate(hypos, {}, None)
    assert evaluated[0]["confidence"] >= 0.65

#!/usr/bin/env python3
"""
Leviathan Engine v2.0 — Working Demo
Confirmed working: initialize, bridge_search, detect_manipulation, get_stats
Confirmed async: semantic_rank, index_bridge_document
"""
import asyncio
from leviathan_engine import LeviathanEngine, SearchResult


async def main():
    print("=" * 60)
    print("LEVIATHAN ENGINE v2.0 — SOVEREIGN SIMULATION")
    print("=" * 60)

    engine = LeviathanEngine()
    await engine.initialize()

    print("\n[1] Engine Stats")
    stats = engine.get_stats()
    print(f"  version: {stats['version']}")
    print(f"  engine_id: {stats['engine_id']}")
    print(f"  master_seal: {stats['master_seal'][:24]}...")
    print(f"  mu_minimum: {stats['config']['mu_minimum']}")
    print(f"  indexed docs: {stats['indexer']['total_documents']}")

    print("\n[2] Bridge Search")
    session = await engine.bridge_search("coherence mu harmony", max_results=5)
    print(f"  Query: 'coherence mu harmony'")
    print(f"  Total results: {len(session.results)}")
    for r in session.results[:3]:
        score = r.mu_aggregate or r.resonance_rank or 0
        print(f"  [{score:.4f}] {r.title[:55]}")

    print("\n[3] Manipulation Detection")
    texts = [
        ("Scientists say coffee is good for you.", "Coffee Claim"),
        ("Study shows coffee causes cancer. Another says it cures it.", "Contradictory"),
        ("mu >= 0.9995 for all coherence operations.", "Coherence Law"),
        ("The government is controlling the weather using HAARP.", "Conspiracy"),
    ]
    for text, title in texts:
        is_manip, types, score = await engine.detect_manipulation(text, title)
        status = "🚨 DETECTED" if is_manip else "✅ CLEAN"
        print(f"  [{status}] '{title}' — score: {score:.6f}")

    print("\n[4] Semantic Rank (async)")
    candidates = [
        SearchResult(result_id="1", title="Resonance Calculus", snippet="mu computation", url="bridge://rc", domain="bridge", resonance_rank=0.8),
        SearchResult(result_id="2", title="Coffee Health", snippet="coffee is healthy", url="bridge://coffee", domain="bridge", resonance_rank=0.7),
        SearchResult(result_id="3", title="Harmony Gate", snippet="mu and coherence gates", url="bridge://hg", domain="bridge", resonance_rank=0.6),
        SearchResult(result_id="4", title="Bridge Core", snippet="constitutional verification", url="bridge://core", domain="bridge", resonance_rank=0.55),
    ]
    reranked = await engine.semantic_rank("resonance calculus mu", candidates)
    for r in reranked[:4]:
        print(f"  [{r.resonance_rank:.4f}] {r.title}")

    print("\n[5] Index & Retrieve")
    await engine.index_bridge_document(
        doc_id="harmony_formula",
        title="Harmony Formula",
        content="S = mu * C, where mu >= 0.9995 for all sovereign operations",
        metadata={"mu_score": 0.9997}
    )
    session2 = await engine.bridge_search("harmony formula mu", max_results=3)
    print(f"  Indexed harmony formula — found: {len(session2.results)} result(s)")
    for r in session2.results[:2]:
        score = r.mu_aggregate or r.resonance_rank or 0
        print(f"  [{score:.4f}] {r.title[:55]}")

    print("\n[6] Master Seal")
    seal = engine.get_master_seal()
    print(f"  {seal[:48]}...")
    print(f"  Mode: SOVEREIGN | SERVERLESS | CLOUDLESS | PHONE-FIRST")

    print("\nGold ripple eternal. ✨")


if __name__ == "__main__":
    asyncio.run(main())